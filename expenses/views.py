from django.shortcuts import render, redirect
from .models import Transaction, Budget, Category
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return redirect('expenses:dashboard')

@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'expenses/dashboard.html', {'transactions': transactions})

@login_required
def add_transaction(request):
    if request.method == 'POST':
        category = Category.objects.get(id=request.POST['category'])
        transaction = Transaction(
            user=request.user,
            category=category,
            transaction_type=request.POST['transaction_type'],
            amount=request.POST['amount'],
            date=request.POST['date'],
            description=request.POST.get('description', ''),
        )
        transaction.save()
        return redirect('expenses:dashboard')

    categories = Category.objects.all()
    return render(request, 'expenses/add_transaction.html', {'categories': categories})

@login_required
def add_expense(request):
    if request.method == 'POST':
        category = Category.objects.get(id=request.POST['category'])
        amount = request.POST['amount']
        date = request.POST['date']
        description = request.POST.get('description', '')

        Transaction.objects.create(
            user=request.user,
            category=category,
            transaction_type='Expense',
            amount=amount,
            date=date,
            description=description,
        )
        return redirect('expenses:dashboard')

    categories = Category.objects.all()
    return render(request, 'expenses/add_transaction.html', {'categories': categories})

@login_required
def view_budget(request):
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'expenses/view_budget.html', {'budgets': budgets})

@login_required
def add_budget(request):
    if request.method == 'POST':
        category = Category.objects.get(id=request.POST['category'])
        amount = request.POST['amount']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

        Budget.objects.create(
            user=request.user,
            category=category,
            amount=amount,
            start_date=start_date,
            end_date=end_date
        )
        return redirect('expenses:view_budget')

    categories = Category.objects.all()
    return render(request, 'expenses/add_budget.html', {'categories': categories})

# @login_required
# def view_report(request):
#     transactions = Transaction.objects.filter(user=request.user)
#     return render(request, 'expenses/report.html', {'transactions': transactions})
