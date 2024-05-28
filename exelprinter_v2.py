import xlsxwriter
from Parser_v2 import array


def writer(parametr):
    book = xlsxwriter.Workbook(r"D:\DevOPS\Python\Parser\parserresult2.xlsx")
    page = book.add_worksheet("Quotes")

    row = 0
    column = 0

    page.set_column("A:A", 70)
    page.set_column("B:B", 30)
    page.set_column("C:C", 50)

    page.write(row, column, "Quote")
    page.write(row, column + 1, "Author")
    page.write(row, column + 2, "Bio")
    row += 1

    try:
        for item in parametr():
            page.write(row, column, item[0])
            page.write(row, column + 1, item[1])
            page.write(row, column + 2, item[2])
            row += 1
    except KeyboardInterrupt:
        print("Script was interrupted, saving collected data to Excel.")
    finally:
        book.close()


writer(array)
