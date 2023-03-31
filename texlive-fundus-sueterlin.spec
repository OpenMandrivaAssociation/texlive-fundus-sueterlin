Name:		texlive-fundus-sueterlin
Version:	26030
Release:	2
Summary:	Sutterlin
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fundus/suetterl
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fundus-sueterlin.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fundus-sueterlin.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fundus-sueterlin.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
