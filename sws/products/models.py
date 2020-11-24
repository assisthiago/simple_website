from datetime import datetime
from django.db import models


CATEGORY_CHOICES = [
    ('boneca', 'Boneca'),
    ('caneta', 'Caneta com ponteira'),
    ('cesta_pregador_roupa', 'Cesta de pregador de roupa'),
    ('cobre_bolo_filo', 'Cobre-bolo de filó'),
    ('cueiro', 'Cueiro'),
    ('lapi', 'Lápis com ponteira'),
    ('namoradeira', 'Namoradeira de janela'),
    ('naninha', 'Naninha'),
    ('pano_prato', 'Pano de prato'),
    ('peso_porta', 'Peso de porta'),
    ('porta_absorvente', 'Porta absorvente'),
    ('porta_agulha', 'Porta agulha'),
    ('porta_calcinha infantil', 'Porta calcinha infantil'),
    ('porta_moeda', 'Porta moeda'),
    ('porta_oculos', 'Porta óculos'),
    ('porta_pao', 'Porta pão'),
    ('porta_papel_higienico', 'Porta papel higiênico'),
    ('puxa_saco', 'Puxa saco'),
    ('saida_banho_atoalhada', 'Saída de banho atoalhada'),
    ('toalha_mao_cozinha', 'Toalhinha de secar a mão de cozinha'),
    ('toalha_mao_infantil', 'Toalhinha de mão infantil'),
    ('touca_atoalhada_cabelo', 'Touca atoalhada pra cabelo'),
]


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    image_1 =  models.ImageField(upload_to='photos/')
    image_2 =  models.ImageField(upload_to='photos/', blank=True)
    image_3 =  models.ImageField(upload_to='photos/', blank=True)
    image_4 =  models.ImageField(upload_to='photos/', blank=True)
    image_5 =  models.ImageField(upload_to='photos/', blank=True)
    image_6 =  models.ImageField(upload_to='photos/', blank=True)
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name
