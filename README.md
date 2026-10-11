<img width="777" height="789" alt="image" src="https://github.com/user-attachments/assets/5cd32ddb-90f8-44f2-a56f-fee621a2a7ef" />
<img width="744" height="793" alt="image" src="https://github.com/user-attachments/assets/0d074bc9-f2c4-4eab-ab12-697ac08ca4db" />

# Platonic Beauty

Django 5 booking + marketing site for a men's/women's salon (US). Passwordless bookings, local SEO, EN/ES.

## Run locally
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py seed_demo        # demo services, stylists, gallery, reviews
python manage.py create_roles     # Owner / Manager / Stylist groups
python manage.py createsuperuser
python manage.py runserver
```
Without `REDIS_URL`, Celery tasks run inline and emails/SMS print to the console.

## Production
`docker compose up --build` starts web, db (PostgreSQL), redis, celery, beat and nginx.
Set `DEBUG=0`, a real `SECRET_KEY`, `SITE_URL`, email and (optionally) Twilio in `.env`.

## SEO
Built in: unique `<title>`/description/keywords per page and language (editable in **Admin > SEO > Page SEO**),
canonical + hreflang links, Open Graph/Twitter cards, `robots` (private pages are `noindex`), `sitemap.xml` with
language alternates, `robots.txt`, and JSON-LD structured data (HairSalon + price list + rating, WebSite,
Service, Person, BlogPosting, BreadcrumbList).
```bash
python manage.py seed_seo              # ready-made copy for the main pages in en/es/fr/fa (uses BUSINESS_NAME / BUSINESS_CITY)
python manage.py seed_seo --overwrite  # reset those entries
```
Set in `.env`: `SITE_URL` (your real https domain), `BUSINESS_*` (name, address, phone - identical to your Google
Business Profile), `GOOGLE_MAPS_URL`, `SOCIAL_URLS`. Then: verify the site in Google Search Console, submit
`https://yourdomain/sitemap.xml`, claim your Google Business Profile, and ask clients for reviews.
Add one **Local landing page** (Admin > SEO) per service + city you want to rank for.

## Translations (English, Spanish, French, Persian)
The site UI is translated in `locale/es`, `locale/fr` and `locale/fa`. Visitors switch with the EN / ES / FR selector in the
header; URLs are `/es/...` and `/fr/...` (English has no prefix).

After changing any text in a template or Python file, run (no GNU gettext needed, works on Windows):
```bash
pip install -r requirements-dev.txt
python tools/i18n.py            # updates locale/*/django.po and compiles django.mo
python tools/i18n.py de         # add a new language (also add it to LANGUAGES in config/settings.py)
```
New strings appear in the `.po` files with an empty `msgstr`; translate them and run the command again.
Emails/SMS, the Flutter app and content typed in the admin (service names, blog posts) are not part of these files.

## Mobile app (Flutter)
`mobile/platonic_beauty/` holds the Flutter app (services, booking with day/time picker, gallery, reviews, my visits).
It uses the JSON API under `/api/v1/` (`apps/api`). Setup steps: `mobile/platonic_beauty/README.md`.

## Tests
`python manage.py test apps`
