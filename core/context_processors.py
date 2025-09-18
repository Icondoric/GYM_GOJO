def header_context(request):
    return {
        "SITE_NAME": "GOYO Gym Shop",
        "CATEGORIES": [
            {"name":"Suplementos","slug":"suplementos"},
            {"name":"Equipos","slug":"equipos"},
            {"name":"Accesorios","slug":"accesorios"},
            {"name":"Ropa","slug":"ropa"},
            {"name":"Ofertas","slug":"ofertas"},
            {"name":"Packs","slug":"packs"},
        ],
    }