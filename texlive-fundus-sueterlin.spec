# revision 26030
# category Package
# catalog-ctan /macros/latex/contrib/fundus/suetterl
# catalog-date 2012-04-18 12:42:25 +0200
# catalog-license lppl1.3
# catalog-version 1.2
Name:		texlive-fundus-sueterlin
Version:	1.2
Release:	11
Summary:	Sutterlin
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fundus/suetterl
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fundus-sueterlin.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fundus-sueterlin.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fundus-sueterlin.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package supports use, in LaTeX, of the MetaFont emulation
of the Sueterlin handwriting fonts The package is distributed
as part of the fundus bundle..

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fundus-sueterlin/suetterl.sty
%doc %{_texmfdistdir}/doc/latex/fundus-sueterlin/suetterl.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fundus-sueterlin/suetterl.dtx
%doc %{_texmfdistdir}/source/latex/fundus-sueterlin/suetterl.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 813552
- Update to latest release.
- Import texlive-fundus-sueterlin
- Import texlive-fundus-sueterlin

