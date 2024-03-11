import argparse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def create_pdf(input_file, output_file, font_name, font_size=10, encoding="utf-8", start_point=(10, 10), line_spacing=14):
    # 读取文本文件内容
    with open(input_file, "r", encoding=encoding) as file:
        text_content = file.read()

    # 创建一个PDF文档
    pdf_canvas = canvas.Canvas(output_file, pagesize=letter)
    
    # 添加字体
    pdfmetrics.registerFont(TTFont('CustomFont', font_name))  # 需要提供相应的 ttf 文件

    # 设置字体
    pdf_canvas.setFont('CustomFont', font_size)
    
    # 获取页面尺寸
    width, height = pdf_canvas._pagesize

    # 按行写入PDF
    lines = text_content.splitlines()
    x_position, y_position = start_point  # 起始坐标位置

    for line in lines:
        pdf_canvas.drawString(x_position, height - y_position, line)
        y_position += line_spacing  # 控制行间距，根据需要调整

    # 关闭PDF文档
    pdf_canvas.save()

if __name__ == "__main__":
    # 使用argparse模块解析命令行参数
    parser = argparse.ArgumentParser(description='Convert text file to PDF.')
    parser.add_argument('--input', default='input.txt', help='Input text file path.')
    parser.add_argument('--output', default='output.pdf', help='Output PDF file path.')
    parser.add_argument('--font-name', default='./simhei.ttf', help='Font file path.')
    parser.add_argument('--font-size', type=int, default=12, help='Font size.')
    parser.add_argument('--encoding', default='utf-8', help='File encoding.')
    parser.add_argument('--line-margin', type=int, default=12, help='Line margin.')
    parser.add_argument('--left-margin', type=int, default=12, help='left margin.')
    parser.add_argument('--top-margin', type=int, default=12, help='top margin.')
    args = parser.parse_args()

    # 生成PDF文件
    #create_pdf(args.input, args.output, args.font_name, args.font_size, args.encoding)
    # 生成PDF文件
    #create_pdf("input.txt", "output.pdf", font_name='./simhei.ttf', font_size=12, encoding="utf-8", start_point=(10, 10), line_spacing=14)
    create_pdf(args.input, args.output, args.font_name, args.font_size, args.encoding, start_point=(args.left_margin, args.top_margin), line_spacing=args.line_margin)
