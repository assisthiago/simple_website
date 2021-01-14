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
    name = models.CharField(max_length=255, verbose_name='Nome')
    description = models.TextField(max_length=255, blank=True, verbose_name='Descrição')
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, verbose_name='Preço')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, verbose_name='Categoria')
    image_1 =  models.ImageField(upload_to='photos/', verbose_name='Imagem principal')
    image_2 =  models.ImageField(upload_to='photos/', blank=True, verbose_name='Segunda imagem')
    image_3 =  models.ImageField(upload_to='photos/', blank=True, verbose_name= 'Terceira imagem')
    image_4 =  models.ImageField(upload_to='photos/', blank=True, verbose_name= 'Quarta imagem')
    image_5 =  models.ImageField(upload_to='photos/', blank=True, verbose_name= 'Quinta imagem')
    image_6 =  models.ImageField(upload_to='photos/', blank=True, verbose_name= 'Sexta imagem')
    wanted = models.BooleanField(default=False, verbose_name='Mais procurados')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    @staticmethod
    def last_arrivals():
        return Product.objects.order_by('-created_at')[:4]

    @staticmethod
    def most_wanted():
        return Product.objects.filter(wanted=True).order_by('-created_at')

    class Meta:
        verbose_name = 'produto'
        verbose_name_plural = 'Lista de produtos'

    def __str__(self):
        return self.name
