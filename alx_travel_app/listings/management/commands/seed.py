from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding sample data...")

        sample_listings = [
            {
                "title": "Beachfront Villa",
                "description": "A beautiful villa overlooking the ocean.",
                "location": "Malibu, California",
                "price_per_night": 320.00
            },
            {
                "title": "Mountain Cabin",
                "description": "Cozy cabin in the mountains with a fireplace.",
                "location": "Aspen, Colorado",
                "price_per_night": 180.00
            },
            {
                "title": "City Loft",
                "description": "Modern loft in the center of the city.",
                "location": "New York, NY",
                "price_per_night": 250.00
            }
        ]

        for data in sample_listings:
            Listing.objects.get_or_create(**data)

        self.stdout.write(self.style.SUCCESS("Database successfully seeded!"))
