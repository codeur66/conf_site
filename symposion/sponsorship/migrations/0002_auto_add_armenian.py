# Generated by Django 2.2.2 on 2019-06-14 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_sponsorship', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benefit',
            name='content_type',
            field=models.CharField(choices=[('simple', 'Simple'), ('listing_text_af', 'Listing Text (Afrikaans)'), ('listing_text_ar', 'Listing Text (Arabic)'), ('listing_text_ast', 'Listing Text (Asturian)'), ('listing_text_az', 'Listing Text (Azerbaijani)'), ('listing_text_bg', 'Listing Text (Bulgarian)'), ('listing_text_be', 'Listing Text (Belarusian)'), ('listing_text_bn', 'Listing Text (Bengali)'), ('listing_text_br', 'Listing Text (Breton)'), ('listing_text_bs', 'Listing Text (Bosnian)'), ('listing_text_ca', 'Listing Text (Catalan)'), ('listing_text_cs', 'Listing Text (Czech)'), ('listing_text_cy', 'Listing Text (Welsh)'), ('listing_text_da', 'Listing Text (Danish)'), ('listing_text_de', 'Listing Text (German)'), ('listing_text_dsb', 'Listing Text (Lower Sorbian)'), ('listing_text_el', 'Listing Text (Greek)'), ('listing_text_en', 'Listing Text (English)'), ('listing_text_en-au', 'Listing Text (Australian English)'), ('listing_text_en-gb', 'Listing Text (British English)'), ('listing_text_eo', 'Listing Text (Esperanto)'), ('listing_text_es', 'Listing Text (Spanish)'), ('listing_text_es-ar', 'Listing Text (Argentinian Spanish)'), ('listing_text_es-co', 'Listing Text (Colombian Spanish)'), ('listing_text_es-mx', 'Listing Text (Mexican Spanish)'), ('listing_text_es-ni', 'Listing Text (Nicaraguan Spanish)'), ('listing_text_es-ve', 'Listing Text (Venezuelan Spanish)'), ('listing_text_et', 'Listing Text (Estonian)'), ('listing_text_eu', 'Listing Text (Basque)'), ('listing_text_fa', 'Listing Text (Persian)'), ('listing_text_fi', 'Listing Text (Finnish)'), ('listing_text_fr', 'Listing Text (French)'), ('listing_text_fy', 'Listing Text (Frisian)'), ('listing_text_ga', 'Listing Text (Irish)'), ('listing_text_gd', 'Listing Text (Scottish Gaelic)'), ('listing_text_gl', 'Listing Text (Galician)'), ('listing_text_he', 'Listing Text (Hebrew)'), ('listing_text_hi', 'Listing Text (Hindi)'), ('listing_text_hr', 'Listing Text (Croatian)'), ('listing_text_hsb', 'Listing Text (Upper Sorbian)'), ('listing_text_hu', 'Listing Text (Hungarian)'), ('listing_text_hy', 'Listing Text (Armenian)'), ('listing_text_ia', 'Listing Text (Interlingua)'), ('listing_text_id', 'Listing Text (Indonesian)'), ('listing_text_io', 'Listing Text (Ido)'), ('listing_text_is', 'Listing Text (Icelandic)'), ('listing_text_it', 'Listing Text (Italian)'), ('listing_text_ja', 'Listing Text (Japanese)'), ('listing_text_ka', 'Listing Text (Georgian)'), ('listing_text_kab', 'Listing Text (Kabyle)'), ('listing_text_kk', 'Listing Text (Kazakh)'), ('listing_text_km', 'Listing Text (Khmer)'), ('listing_text_kn', 'Listing Text (Kannada)'), ('listing_text_ko', 'Listing Text (Korean)'), ('listing_text_lb', 'Listing Text (Luxembourgish)'), ('listing_text_lt', 'Listing Text (Lithuanian)'), ('listing_text_lv', 'Listing Text (Latvian)'), ('listing_text_mk', 'Listing Text (Macedonian)'), ('listing_text_ml', 'Listing Text (Malayalam)'), ('listing_text_mn', 'Listing Text (Mongolian)'), ('listing_text_mr', 'Listing Text (Marathi)'), ('listing_text_my', 'Listing Text (Burmese)'), ('listing_text_nb', 'Listing Text (Norwegian Bokmål)'), ('listing_text_ne', 'Listing Text (Nepali)'), ('listing_text_nl', 'Listing Text (Dutch)'), ('listing_text_nn', 'Listing Text (Norwegian Nynorsk)'), ('listing_text_os', 'Listing Text (Ossetic)'), ('listing_text_pa', 'Listing Text (Punjabi)'), ('listing_text_pl', 'Listing Text (Polish)'), ('listing_text_pt', 'Listing Text (Portuguese)'), ('listing_text_pt-br', 'Listing Text (Brazilian Portuguese)'), ('listing_text_ro', 'Listing Text (Romanian)'), ('listing_text_ru', 'Listing Text (Russian)'), ('listing_text_sk', 'Listing Text (Slovak)'), ('listing_text_sl', 'Listing Text (Slovenian)'), ('listing_text_sq', 'Listing Text (Albanian)'), ('listing_text_sr', 'Listing Text (Serbian)'), ('listing_text_sr-latn', 'Listing Text (Serbian Latin)'), ('listing_text_sv', 'Listing Text (Swedish)'), ('listing_text_sw', 'Listing Text (Swahili)'), ('listing_text_ta', 'Listing Text (Tamil)'), ('listing_text_te', 'Listing Text (Telugu)'), ('listing_text_th', 'Listing Text (Thai)'), ('listing_text_tr', 'Listing Text (Turkish)'), ('listing_text_tt', 'Listing Text (Tatar)'), ('listing_text_udm', 'Listing Text (Udmurt)'), ('listing_text_uk', 'Listing Text (Ukrainian)'), ('listing_text_ur', 'Listing Text (Urdu)'), ('listing_text_vi', 'Listing Text (Vietnamese)'), ('listing_text_zh-hans', 'Listing Text (Simplified Chinese)'), ('listing_text_zh-hant', 'Listing Text (Traditional Chinese)')], default='simple', max_length=20, verbose_name='content type'),
        ),
    ]
