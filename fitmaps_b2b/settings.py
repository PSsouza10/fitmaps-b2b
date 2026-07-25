# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Adicione esta linha logo abaixo para o WhiteNoise compactar e servir os estáticos corretamente em produção:
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'