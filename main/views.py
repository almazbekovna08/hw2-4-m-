from django.shortcuts import render

# Create your views here.
def cosmetics(request):
    context={
        "title":"Cosmetics❤️",
        "type": "✨ Набор для ежедневного макияжа ✨",
        "description1": "💖 Все, что нужно для твоего идеального образа:",
        "description2":"🌟 Пудра для матового эффекта и свежего вида",
        "description3":"💛 Золотистый хайлайтер для сияния и акцента на самых красивых чертах",
        "description4":"🎨 Кисть 5 в 1 – универсальный инструмент, который заменит несколько аксессуаров",
        "motivation": "Создавай легкий и естественный макияж каждый день 🌷. Будь безупречна в любое время! 💄"
    }
    
    return render(request, 'index.html', context=context)

