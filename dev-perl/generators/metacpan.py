#!/usr/bin/env python3

from bs4 import BeautifulSoup
from packaging.version import Version
import re

async def generate(hub, **pkginfo):
	homepage = f"https://metacpan.org/pod/{pkginfo['name'].replace('-', '::')}"
	regex = r'(\d+(?:\.\d+)+)'
	html = await hub.pkgtools.fetch.get_page(homepage)
	soup = BeautifulSoup(html, "html.parser").find("li", class_="version-jump").find_all("option")

	options = [opt.get('value').split('/') for opt in soup if opt and opt.get('value')]

	versions = [(re.findall(regex, a[1])[0], a[0]) for a in options]
	latest = max([(Version(v[0]), v[0], v[1]) for v in versions])

	links = BeautifulSoup(html, "html.parser").find_all("a")
	download_url = [a.get('href') for a in links if a.get('href') and '.tar.' in a.get('href')][0]

	ebuild = hub.pkgtools.ebuild.BreezyBuild(
		**pkginfo,
		version = latest[0],
		dist_version = latest[1],
		dist_author = latest[2],
		artifacts=[hub.pkgtools.ebuild.Artifact(url=download_url)]
	)
	ebuild.push()

# vim: ts=4 sw=4 noet
