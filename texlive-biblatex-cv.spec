%global tl_name biblatex-cv
%global tl_revision 59433

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.01
Release:	%{tl_revision}.1
Summary:	Create a CV from BibTeX files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-cv
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-cv.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-cv.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package creates an academic curriculum vitae (CV) from a BibTeX
.bib file. The package makes use of BibLaTeX/biber to automatically
format, group, and sort the entries on a CV.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-cv
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-cv
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-cv/README.md
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-cv/biblatex-cv.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-cv/biblatex-cv.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-cv/biblatex-cv.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-cv/cv.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-cv/cv.tex
%{_datadir}/texmf-dist/tex/latex/biblatex-cv/american-cv.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-cv/biblatex-cv.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-cv/biblatex-cv.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-cv/biblatex-cv.dbx
%{_datadir}/texmf-dist/tex/latex/biblatex-cv/biblatex-cv.sty
