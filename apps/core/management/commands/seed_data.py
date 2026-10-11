from django.core.management.base import BaseCommand
from apps.services.models import Service, ServiceCategory
from apps.stylists.models import Stylist
from apps.gallery.models import GalleryItem
from apps.blog.models import BlogPost
from django.utils import timezone


class Command(BaseCommand):
    """
    Seed initial data for PlatonicBeauty.
    Usage: python manage.py seed_data
    """
    help = 'Populate the database with initial demo data.'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')

        # --- Service Categories ---
        cats = [
            ('Haircut', 'haircut', 1),
            ('Coloring', 'coloring', 2),
            ('Spa & Treatment', 'spa-treatment', 3),
        ]
        for name, slug, order in cats:
            ServiceCategory.objects.get_or_create(
                slug=slug,
                defaults={'name': name, 'order': order}
            )

        # --- Services ---
        cat_haircut = ServiceCategory.objects.get(slug='haircut')
        cat_coloring = ServiceCategory.objects.get(slug='coloring')
        cat_spa = ServiceCategory.objects.get(slug='spa-treatment')

        services = [
            ('Men\'s Haircut', 'mens-haircut', 'Classic men\'s haircut with consultation, wash, and styling.', 'male', cat_haircut, 30, '35.00'),
            ('Men\'s Beard Trim', 'mens-beard-trim', 'Professional beard shaping and trim with hot towel.', 'male', cat_haircut, 20, '25.00'),
            ('Women\'s Cut & Style', 'womens-cut-style', 'Precision women\'s haircut with wash, blow-dry, and styling.', 'female', cat_haircut, 60, '75.00'),
            ('Balayage', 'balayage', 'Hand-painted highlights for a natural, sun-kissed look.', 'female', cat_coloring, 180, '220.00'),
            ('Full Color', 'full-color', 'Complete hair coloring with premium products.', 'unisex', cat_coloring, 120, '150.00'),
            ('Deep Conditioning Treatment', 'deep-conditioning', 'Intensive moisturizing treatment for damaged hair.', 'unisex', cat_spa, 45, '60.00'),
        ]
        for name, slug, desc, gender, cat, dur, price in services:
            Service.objects.get_or_create(
                slug=slug,
                defaults={
                    'name': name,
                    'description': desc,
                    'gender': gender,
                    'category': cat,
                    'duration_minutes': dur,
                    'price': price,
                    'is_active': True,
                }
            )

        # --- Stylists ---
        stylists = [
            ('Alex Morgan', 'alex-morgan', 'Master barber with 10 years of experience.', 1),
            ('Sofia Laurent', 'sofia-laurent', 'Color specialist trained in Paris.', 2),
            ('Jordan Blake', 'jordan-blake', 'Unisex stylist with a passion for precision cuts.', 3),
            ('Mia Chen', 'mia-chen', 'Spa and treatment expert.', 4),
        ]
        for name, slug, bio, order in stylists:
            Stylist.objects.get_or_create(
                slug=slug,
                defaults={
                    'display_name': name,
                    'bio': bio,
                    'is_active': True,
                    'order': order,
                }
            )

        # --- Gallery ---
        gallery_items = [
            ('Classic Men\'s Fade', 'hair', 'male', 1),
            ('Balayage Transformation', 'hair', 'female', 2),
            ('Bridal Updo', 'hair', 'female', 3),
            ('Beard Grooming', 'hair', 'male', 4),
        ]
        for title, cat, gender, order in gallery_items:
            GalleryItem.objects.get_or_create(
                title=title,
                defaults={
                    'category': cat,
                    'gender': gender,
                    'is_active': True,
                    'order': order,
                }
            )

        # --- Blog Posts ---
        posts = [
            ('5 Tips for Healthy Hair in Winter', '5-tips-healthy-hair-winter',
             'Cold weather can dry out your hair.', 'Winter is tough on hair...'),
            ('Balayage vs. Highlights', 'balayage-vs-highlights',
             'Not sure which coloring technique is right for you?', 'Balayage and highlights...'),
            ('How to Prepare for Your Salon Visit', 'prepare-salon-visit',
             'A few simple steps before your appointment.', 'Coming prepared...'),
        ]
        for title, slug, excerpt, content in posts:
            BlogPost.objects.get_or_create(
                slug=slug,
                defaults={
                    'title': title,
                    'excerpt': excerpt,
                    'content': content,
                    'is_published': True,
                    'published_at': timezone.now(),
                }
            )

        self.stdout.write(self.style.SUCCESS('✓ Demo data seeded successfully!'))