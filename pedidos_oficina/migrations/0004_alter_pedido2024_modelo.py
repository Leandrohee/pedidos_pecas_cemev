# Generated by Django 5.0.3 on 2024-03-27 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos_oficina', '0003_alter_pedido2024_prefixo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido2024',
            name='modelo',
            field=models.CharField(choices=[('1', '13.18'), ('2', 'RENEGADE 1.8 AUTOM.'), ('3', 'TRANSIT 350L'), ('4', '15.18'), ('5', 'SPRINTER C'), ('6', 'L200 TRITON 3.2 D'), ('7', 'ITURRI P360'), ('8', 'SPRINTER'), ('9', 'CARGO 712'), ('10', 'GRANMIDI '), ('11', 'DAILY 70C16HDCS'), ('12', 'RD1 158'), ('13', '15.190 CRM 4X2'), ('14', 'S10 LTZ '), ('15', 'GRAND VIA'), ('16', 'ATEGO 823'), ('17', 'ATEGO 1729'), ('18', 'ARGO '), ('19', 'KANGOO '), ('20', 'CRUZE LT'), ('21', 'RANGER '), ('22', 'SANDERO DYNA 1.6'), ('23', '2031 ACTROS'), ('24', 'M.BENZ 516 MOBILE S. CM'), ('25', 'O 500RSD'), ('26', 'DAILY 70C16'), ('27', 'SPRINTER 415'), ('28', 'ACCELO 815'), ('29', 'HILUX '), ('30', 'C4'), ('31', 'ATEGO 3330CE'), ('32', 'XT 660R'), ('33', 'CARGO 1519 S'), ('34', 'PALIO ESSENCE 1.6'), ('35', 'INDUSCAR GI R 500'), ('36', '31.330  6X4'), ('37', 'CARRETA'), ('38', '17250 CNC'), ('39', 'G650 GS'), ('40', 'CB 500X'), ('41', 'LOGAN EXP 16'), ('42', 'XRE 300'), ('43', 'UNO '), ('44', 'P 440 MAGIRUS'), ('45', '1030'), ('46', '19.390 4X2'), ('47', 'JACINTO P-360'), ('48', 'ATEGO 1726/42'), ('49', 'PAJERO HD'), ('50', '31.32'), ('51', '380T38'), ('52', 'XTZ 250'), ('53', 'MASCA GRANMINI O'), ('54', 'VOLARE A6'), ('55', '3331 ACTROS'), ('56', 'FURGOVAN 6000'), ('57', '170 E 22'), ('58', 'ATEGO 1725'), ('59', 'GIMAEX P360'), ('60', 'L200 TRITON'), ('61', 'ARROW XT'), ('62', '70C16HDCS'), ('63', 'CARGO 2622 E'), ('64', 'ITURRI P320'), ('65', 'PIÁ'), ('66', '4140 ACTROS'), ('67', 'S10 LT '), ('68', '17.21')], max_length=30),
        ),
    ]
