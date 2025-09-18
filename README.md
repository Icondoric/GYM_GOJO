# GOYO – Gym E‑commerce (Django skeleton)

Este esqueleto funcional implementa el *MVP* para GOYO: catálogo (suplementos, equipamiento, ropa), carrito, checkout simple, blog y cuentas (allauth). Visual minimalista, listo para iterar UI/UX.

## Requisitos
- Python 3.11+
- pip + venv
- (Opcional) Node para front avanzado más adelante

## Instalación rápida
```bash
python -m venv .venv && source .venv/bin/activate  # en Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata fixtures_sample.json
python manage.py createsuperuser
python manage.py runserver
```

Visita:
- Home: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Rutas principales
- `catalog/c/<slug>/` — PLP por categoría (filtros básicos por querystring)
- `catalog/p/<slug>/` — PDP con variantes, ingredientes y especificaciones
- `cart/` — Carrito (session‑based) + `cart/add/<variant_id>/`
- `orders/checkout/` — Checkout 1 paso (dirección + creación pedido)
- `orders/success/<order_id>/` — Confirmación
- `blog/` — Listado básico y detalle
- `accounts/` — Login/registro con allauth
- `memberships/` — Landing suscripciones (placeholder)
- `legal/<slug>/` — Páginas legales placeholder

## Próximos pasos (mapeo con tu requerimiento)

- Header sticky + mini‑carrito, mega‑menú visual, badges, bento grid → **templates + CSS**.
- Filtros avanzados (marca/objetivo/tipo/sabor/talla/precio/rating/stock) → **catalog.views.CategoryPLP**: ampliar filtros y ordenar.
- Comparador suplementos/equipos → **catalog.CompareList** ya creado (activar UI).
- Bundles/Packs → **catalog.Bundle** + vista/plantilla.
- Timer ofertas relámpago → componente JS simple + flag en modelos/promotions.
- Tabla de ingredientes / carga máxima → **Ingredient** / **Spec** en PDP (ya listo).
- Reviews + Q&A verificados → **reviews.models** + formularios y permisos.
- Checkout 2 pasos, cupones/gift cards, envío/impuestos, tokenización pagos, RMA estados, notificaciones, suscripciones → modelos base listos en *orders*, *promotions*, *subscriptions*: conectar con pasarelas (Stripe/PayPal/Adyen o regional), couriers y notificaciones (Sendgrid/Twilio/WA).
- Búsqueda con autocomplete/sinónimos → endpoint `/search/` (placeholder); integrar Algolia/Meilisearch.
- Analytics (embudos/cohortes/LTV) → hooks de server‑side events + GA4/Meta/TikTok.
- Seguridad (HTTPS, CSP, HSTS, rate‑limit, 2FA admin) → configurar en `settings.py` y reverse proxy.
- SEO/Performance → imágenes WebP/AVIF con Pillow, sitemap/robots, datos estructurados.
- PWA → app manifest + service worker (front).

---

> Este repo es un punto de partida *funcional*. Permite navegar categorías (PLP), ver productos (PDP), agregar al carrito y generar un pedido. Desde aquí iteramos lo visual y añadimos integraciones.