# Distributed under the terms of the GNU General Public License v2

EAPI=7

DIST_AUTHOR=ZEFRAM
DIST_VERSION=0.003
inherit perl-module
IUSE="test"
DESCRIPTION="Deconstructed Dynamic C Library Loading"
SLOT="0"
KEYWORDS="*"

RDEPEND="
	virtual/perl-Carp
	virtual/perl-Exporter
	virtual/perl-XSLoader
	dev-perl/Module-Build
"
BDEPEND="${RDEPEND}
	test? (
		virtual/perl-Test-Simple
	)
"
DEPEND="${RDEPEND}"
