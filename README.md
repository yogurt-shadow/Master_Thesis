使用说明: [original.md](original.md)

## VSCode中生成参考文献 (bibTex)
根目录的Thesis.bbl会显示用到的参考文献目录，一般用bibtex生成。
具体命令如下：
```bash
pdflatex Thesis.tex
bibtex Thesis.aux
pdflatex Thesis.tex
pdflatex Thesis.tex
```


## 结构：
- [参考文献](Biblio/ref.bib): bibtex格式的参考文献。
- [基本信息](Tex/Frontinfo.tex): 包含作者、导师、日期、学校、专业、题目、摘要等基本信息。
- [摘要](Tex/Frontmatter.tex)：摘要部分。
- [第1章 绪论](Tex/Chap_Intro.tex): 介绍本文的背景、目的、研究意义、研究方法、研究范围、研究内容、研究成果、研究意义等。