from django.core.mail import send_mail
from django.shortcuts import redirect, render

from practice.forms import ExchangeForm


def send_msg(email, name, title, artist, genre, price, comment):
    subject = f"Обмен {artist}-{title}"
    body = f"""Предложение на обмен диска от {name} ({email})

    Название: {title}
    Исполнитель: {artist}
    Жанр: {genre}
    Стоимость: {price}
    Комментарий: {comment}

    """
    send_mail(
        subject, body, email, ["admin@rockenrolla.net", ],
    )


def index(request):
    if request.method == 'POST':
        form = ExchangeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            title = form.cleaned_data['title']
            artist = form.cleaned_data['name']
            genre = form.cleaned_data['genre']
            price = form.cleaned_data['price']
            comment = form.cleaned_data['comment']
            send_msg(email, name, title, artist, genre, price, comment)
            return redirect('/thankyou/')
        return render(request, 'index.html', {'form': form})
    form = ExchangeForm()
    return render(request, 'index.html', {'form': form})

def thankyou(request):
    return render(request, 'thankyou.html')
