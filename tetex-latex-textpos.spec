
%define short_name textpos

Summary:	Lay out text and graphics at arbitrary positions on the LaTeX page
Summary(pl):	Umieszczanie tekstu i grafiki w dowolnej pozycji na stronia LaTeXa
Name:		tetex-latex-%{short_name}
Version:	1.4
Release:	1
License:	GPL
Group:		Applications/Publishing/TeX
Source0:	http://www.astro.gla.ac.uk/users/norman/distrib/latex/%{short_name}-%{version}.tar.gz
# Source0-md5:	f8f347198edffc8a6f72f386579d9154
URL:		http://www.astro.gla.ac.uk/users/norman/distrib/latex/#textpos
BuildRequires:	tetex-format-pdflatex
Requires(post,postun):	/usr/bin/texhash
Requires:	tetex-latex
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

%description
This package facilitates placing boxes at absolute positions on the
LaTeX page. There are several reasons why this might be useful, but
the main one (or at least my motivating one) is to help produce a
large-format conference poster.

%description -l pl
Ten pakiet u³atwia umieszczanie pude³ek w absolutnym po³o¿eniu na
stronie LaTeXa. Jest kilkana¶cie powodów dlaczego to mo¿e byæ
u¿yteczne, ale g³ównym (albo przynajmniej tym motywuj±cym) jest pomóc
w produkcji wielkoformatowego plakatu konferencji.

%prep
%setup -q -n %{short_name}-%{version}

%build
latex textpos.ins
pdflatex textpos.dtx

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/{tex,doc}/latex/%{short_name}

install *.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}
install *.pdf $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc README
%{_datadir}/texmf/tex/latex/%{short_name}/*
%doc %{_datadir}/texmf/doc/latex/%{short_name}/*
