import os
for root, dirs, files in os.walk("E:\Gurov_SSD_256"):
    for file in files:
        res = ''
        file_res = open("E:\Gurov_SSD_256\IT\Testing\Automation_08_09_2019\scraping\\file_res.txt", "a")
        if file.endswith(".pdf"):
             res += (os.path.join(root, file, "\n"))
             n = file_res.write(res)
             file_res.close()
             print(res, n)