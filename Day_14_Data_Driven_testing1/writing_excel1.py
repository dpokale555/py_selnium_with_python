import openpyxl

file="C:\\Users\\dhananjay.pokale\\Desktop\MyPersonal\\Python_DurgaSoft\\test_file.xlsx"
workbook=openpyxl.load_workbook((file))
sheet=workbook["Data"]    #If file have multiple sheets than use this
# sheet=workbook.active   #If file have only single sheet is avalible than use this

#Example 1: Write the same value in excel
for r in range(1,6):
    for c in range(1,4):
        sheet.cell(r,c).value="Home"

workbook.save(file)

