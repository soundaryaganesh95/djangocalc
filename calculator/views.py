from django.shortcuts import render

def calculator_view(request):
    # Default values
    result = None
    context = {}

    if request.method == 'POST':
        try:
            # Note: We are only showing the result display, 
            # so the actual math logic is simplified for this example.
            num1 = float(request.POST.get('num1', 0))
            num2 = float(request.POST.get('num2', 0))
            operation = request.POST.get('operation')
            
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                # Basic error handling for division by zero
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error: Div by Zero"

            # Prepare context with the result and the input values for display
            context = {
                'result': result,
                'num1': num1,
                'num2': num2,
                'operation': operation,
            }

        except ValueError:
            context['error'] = "Invalid input. Please enter numbers."
            
    return render(request, 'calculator/calc.html', context)