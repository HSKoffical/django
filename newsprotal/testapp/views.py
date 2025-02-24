from django.shortcuts import render
def main(request):
    return render(request,'testapp/main.html')

def sport(request):
    news1='Virat kholi score 82 century aginst pakistan'
    news2='India is in the final'
    news3='India won aginst pakistan by 5 wicktes'
    mydict={'news1':news1,'news2':news2,'news3':news3}
    return render(request,'testapp/sport.html',mydict)
def polities(request):
    news1='Bjp won the election in Delhi'
    news2='The new CM of delhi is rehka gupta'
    news3='The leader of india is PM Nerandra Modi sir'
    mydict={'news1':news1,'news2':news2,'news3':news3}
    return render(request,'testapp/polities.html',mydict)
def movies(request):
    news1='Chavaa movie successfully cross the mark of 400 cr in collection'
    news2='Chavaa movie is biggest hit of 2025'
    news3='The marvel next big movie is thenderboults'
    mydict={'news1':news1,'news2':news2,'news3':news3}
    return render(request,'testapp/movies.html',mydict)