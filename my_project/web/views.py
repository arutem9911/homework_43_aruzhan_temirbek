from django.shortcuts import render


def calculate_view(request):
    if request.method == 'GET':
        return render(request, 'input_forms.html')

    elif request.method == 'POST':
        number1, number2 = request.POST.getlist('numbers')
        operation = request.POST['operation']

        if operation == 'add':
            symbol = '+'
            result = int(number1) + int(number2)
        elif operation == 'subtract':
            symbol = '-'
            result = int(number1) - int(number2)
        elif operation == 'multiply':
            symbol = '*'
            result = int(number1) * int(number2)
        else:
            symbol = '/'
            result = int(number1) / int(number2)

        return render(request, 'result.html', context={
            'number1': number1,
            'number2': number2,
            'operation': operation,
            'symbol': symbol,
            'result': result
        })

