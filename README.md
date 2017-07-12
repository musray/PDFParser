# PDFParser

## 参考：
1. 一个使用pdfminer的[blog post](https://dzone.com/articles/pdf-reading)
2. adobe官方的[pdf参考](http://www.adobe.com/devnet/pdf/pdf_reference.html)
3. 一个好像真的很适合我使用的library - [PyMuPDF](https://pythonhosted.org/PyMuPDF/annot.html#example)

## 神器 - `PyMuPDF`
啥也不说了，PyMuPDF基本可以满足我基于PDF二次开发的所有需求。
激动的我都想给开发者捐款。

## PDFParser
尝试对PDF进行操作，包括：
1. 页内文本提取
2. 页操作 - 提取、删除、插入、排序
3. 标注页眉
4. 标注（Annotation）的操作
    - 基本图形（对方形、圆形、云线）的信息获取，包括图形自身的备注(popup)信息
    - 文本框的信息获取
5. 多文件操作
    - 从多个文件中提取指定页面
    - 合并为一个文件
