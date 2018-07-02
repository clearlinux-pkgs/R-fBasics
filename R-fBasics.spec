#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fBasics
Version  : 3042.89
Release  : 4
URL      : https://cran.r-project.org/src/contrib/fBasics_3042.89.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fBasics_3042.89.tar.gz
Summary  : Rmetrics - Markets and Basic Statistics
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-fBasics-lib
Requires: R-gss
Requires: R-stabledist
Requires: R-timeDate
Requires: R-timeSeries
BuildRequires : R-gss
BuildRequires : R-stabledist
BuildRequires : R-timeDate
BuildRequires : R-timeSeries
BuildRequires : clr-R-helpers

%description
explore and to investigate basic properties of financial returns 
    and related quantities.
    The covered fields include techniques of explorative data analysis
    and the investigation of distributional properties, including
    parameter estimation and hypothesis testing. Even more there are
    several utility functions for data handling and management.

%package lib
Summary: lib components for the R-fBasics package.
Group: Libraries

%description lib
lib components for the R-fBasics package.


%prep
%setup -q -c -n fBasics

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530456693

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530456693
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fBasics
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fBasics
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fBasics
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library fBasics|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fBasics/DESCRIPTION
/usr/lib64/R/library/fBasics/INDEX
/usr/lib64/R/library/fBasics/Meta/Rd.rds
/usr/lib64/R/library/fBasics/Meta/data.rds
/usr/lib64/R/library/fBasics/Meta/features.rds
/usr/lib64/R/library/fBasics/Meta/hsearch.rds
/usr/lib64/R/library/fBasics/Meta/links.rds
/usr/lib64/R/library/fBasics/Meta/nsInfo.rds
/usr/lib64/R/library/fBasics/Meta/package.rds
/usr/lib64/R/library/fBasics/NAMESPACE
/usr/lib64/R/library/fBasics/R/fBasics
/usr/lib64/R/library/fBasics/R/fBasics.rdb
/usr/lib64/R/library/fBasics/R/fBasics.rdx
/usr/lib64/R/library/fBasics/data/Rdata.rdb
/usr/lib64/R/library/fBasics/data/Rdata.rds
/usr/lib64/R/library/fBasics/data/Rdata.rdx
/usr/lib64/R/library/fBasics/help/AnIndex
/usr/lib64/R/library/fBasics/help/aliases.rds
/usr/lib64/R/library/fBasics/help/fBasics.rdb
/usr/lib64/R/library/fBasics/help/fBasics.rdx
/usr/lib64/R/library/fBasics/help/paths.rds
/usr/lib64/R/library/fBasics/html/00Index.html
/usr/lib64/R/library/fBasics/html/R.css
/usr/lib64/R/library/fBasics/libs/symbols.rds
/usr/lib64/R/library/fBasics/unitTests/HeavisideSlider.R
/usr/lib64/R/library/fBasics/unitTests/Makefile
/usr/lib64/R/library/fBasics/unitTests/runTests.R
/usr/lib64/R/library/fBasics/unitTests/runit.DistributionFits.R
/usr/lib64/R/library/fBasics/unitTests/runit.Heaviside.R
/usr/lib64/R/library/fBasics/unitTests/runit.HyperbolicDistribution.R
/usr/lib64/R/library/fBasics/unitTests/runit.JarqueBeraPValues.R
/usr/lib64/R/library/fBasics/unitTests/runit.NormalityTests.R
/usr/lib64/R/library/fBasics/unitTests/runit.ReturnSeriesBasics.R
/usr/lib64/R/library/fBasics/unitTests/runit.StylizedFacts.R
/usr/lib64/R/library/fBasics/unitTests/runit.Sys.putenv.R
/usr/lib64/R/library/fBasics/unitTests/runit.TwoSampleTests.R
/usr/lib64/R/library/fBasics/unitTests/runit.akimaInterp.R
/usr/lib64/R/library/fBasics/unitTests/runit.as.matrix.ts.R
/usr/lib64/R/library/fBasics/unitTests/runit.asPOSIXlt.R
/usr/lib64/R/library/fBasics/unitTests/runit.baseMethods.R
/usr/lib64/R/library/fBasics/unitTests/runit.characterTable.R
/usr/lib64/R/library/fBasics/unitTests/runit.colStats.R
/usr/lib64/R/library/fBasics/unitTests/runit.colorLocator.R
/usr/lib64/R/library/fBasics/unitTests/runit.colorPalette.R
/usr/lib64/R/library/fBasics/unitTests/runit.colorTable.R
/usr/lib64/R/library/fBasics/unitTests/runit.decor.R
/usr/lib64/R/library/fBasics/unitTests/runit.description.R
/usr/lib64/R/library/fBasics/unitTests/runit.distCheck.R
/usr/lib64/R/library/fBasics/unitTests/runit.fHTEST.R
/usr/lib64/R/library/fBasics/unitTests/runit.getS4.R
/usr/lib64/R/library/fBasics/unitTests/runit.gridVector.R
/usr/lib64/R/library/fBasics/unitTests/runit.interactivePlot.R
/usr/lib64/R/library/fBasics/unitTests/runit.julian.R
/usr/lib64/R/library/fBasics/unitTests/runit.krigeInterp.R
/usr/lib64/R/library/fBasics/unitTests/runit.kurtosis.R
/usr/lib64/R/library/fBasics/unitTests/runit.lcg.R
/usr/lib64/R/library/fBasics/unitTests/runit.linearInterp.R
/usr/lib64/R/library/fBasics/unitTests/runit.listDescription.R
/usr/lib64/R/library/fBasics/unitTests/runit.listFunctions.R
/usr/lib64/R/library/fBasics/unitTests/runit.listIndex.R
/usr/lib64/R/library/fBasics/unitTests/runit.matrixAddon.R
/usr/lib64/R/library/fBasics/unitTests/runit.plot.R
/usr/lib64/R/library/fBasics/unitTests/runit.print.R
/usr/lib64/R/library/fBasics/unitTests/runit.rgb.R
/usr/lib64/R/library/fBasics/unitTests/runit.rowStats.R
/usr/lib64/R/library/fBasics/unitTests/runit.skewness.R
/usr/lib64/R/library/fBasics/unitTests/runit.sliderMenu.R
/usr/lib64/R/library/fBasics/unitTests/runit.subPlot.R
/usr/lib64/R/library/fBasics/unitTests/runit.subStars.R
/usr/lib64/R/library/fBasics/unitTests/runit.symbolTable.R
/usr/lib64/R/library/fBasics/unitTests/runit.unitrootNA.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/fBasics/libs/fBasics.so
/usr/lib64/R/library/fBasics/libs/fBasics.so.avx2
/usr/lib64/R/library/fBasics/libs/fBasics.so.avx512
