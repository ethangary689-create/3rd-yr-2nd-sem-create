import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from assets.models import Asset, MaintenanceLog, User


class Command(BaseCommand):
    help = 'Seeds the database with 15 sample assets and 5 maintenance logs'

    def handle(self, *args, **options):
        # Create a default user if none exists
        user, created = User.objects.get_or_create(
            username='admin_user',
            defaults={
                'role': 'ADMIN',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        if created:
            user.set_password('admin123')
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Created admin user: admin_user / admin123'))

        # Create a second user for assignment variety
        user2, created2 = User.objects.get_or_create(
            username='john_doe',
            defaults={'role': 'EMPLOYEE'}
        )
        if created2:
            user2.set_password('employee123')
            user2.save()
            self.stdout.write(self.style.SUCCESS(f'Created employee user: john_doe'))

        user3, created3 = User.objects.get_or_create(
            username='jane_smith',
            defaults={'role': 'MANAGER'}
        )
        if created3:
            user3.set_password('manager123')
            user3.save()
            self.stdout.write(self.style.SUCCESS(f'Created manager user: jane_smith'))

        users = [user, user2, user3, None]  # None = unassigned

        # Sample asset data
        asset_data = [
            ('Dell Latitude 5540', 'LAPTOP', 1299.99),
            ('MacBook Pro 16"', 'LAPTOP', 2499.00),
            ('ThinkPad X1 Carbon', 'LAPTOP', 1599.50),
            ('HP EliteBook 840', 'LAPTOP', 1149.00),
            ('Dell UltraSharp 27"', 'MONITOR', 549.99),
            ('LG 34" Curved Monitor', 'MONITOR', 799.00),
            ('Samsung 24" Monitor', 'MONITOR', 329.99),
            ('ASUS ProArt Display', 'MONITOR', 679.00),
            ('iPhone 15 Pro', 'PHONE', 999.99),
            ('Samsung Galaxy S24', 'PHONE', 849.00),
            ('Google Pixel 8', 'PHONE', 699.00),
            ('Standing Desk - Large', 'FURNITURE', 899.99),
            ('Herman Miller Aeron Chair', 'FURNITURE', 1395.00),
            ('Filing Cabinet 4-Drawer', 'FURNITURE', 249.99),
            ('Conference Table 8ft', 'FURNITURE', 1799.00),
        ]

        assets = []
        for name, asset_type, cost in asset_data:
            asset, created = Asset.objects.get_or_create(
                name=name,
                defaults={
                    'asset_type': asset_type,
                    'cost': cost,
                    'assigned_to': random.choice(users),
                }
            )
            assets.append(asset)
            if created:
                self.stdout.write(f'  Created asset: {name}')

        self.stdout.write(self.style.SUCCESS(f'Total assets in DB: {Asset.objects.count()}'))

        # Sample maintenance logs
        maintenance_data = [
            (assets[0], date(2025, 6, 15), 'Replaced battery and keyboard. Full diagnostic performed.', 285.00),
            (assets[1], date(2025, 8, 22), 'Screen replacement due to crack. AppleCare claim processed.', 450.00),
            (assets[4], date(2025, 3, 10), 'Fixed dead pixels. Firmware update applied.', 120.00),
            (assets[8], date(2025, 11, 5), 'Replaced cracked screen protector and recalibrated touchscreen.', 89.99),
            (assets[12], date(2026, 1, 18), 'Replaced hydraulic cylinder and armrest pads. Cleaned mesh.', 175.50),
        ]

        for asset, svc_date, desc, cost in maintenance_data:
            log, created = MaintenanceLog.objects.get_or_create(
                asset=asset,
                service_date=svc_date,
                defaults={
                    'description': desc,
                    'cost': cost,
                }
            )
            if created:
                self.stdout.write(f'  Created maintenance log for: {asset.name}')

        self.stdout.write(self.style.SUCCESS(f'Total maintenance logs in DB: {MaintenanceLog.objects.count()}'))
        self.stdout.write(self.style.SUCCESS('Database seeding complete!'))
