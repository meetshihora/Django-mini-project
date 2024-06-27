from django.shortcuts import render

def marksheet(request):
    if request.method == 'POST':
        subject1 = eval(request.POST.get('subject1'))
        subject2 = eval(request.POST.get('subject2'))
        subject3 = eval(request.POST.get('subject3'))
        subject4 = eval(request.POST.get('subject4'))
        subject5 = eval(request.POST.get('subject5'))
        total_marks = subject1 + subject2 + subject3 + subject4 + subject5
        percentage = (total_marks / 500) * 100
        if percentage >= 80:
            grade = "A+"
        elif percentage >= 70:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "Fail"
        context = {
            'total_marks': total_marks,
            'percentage': percentage,
            'grade': grade
        }
        return render(request, 'marksheet.html', context)
    return render(request, 'marksheet.html')