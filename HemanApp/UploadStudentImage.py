def uploaded_file(f):  
    with open('HemanApp/static/student/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  