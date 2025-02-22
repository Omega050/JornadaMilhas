from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from jornada.models import Depoimento
from jornada.serializers import DepoimentoSerializer

class SerializerDepoimentoTestCase(TestCase):
    def setUp(self):
        image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b"\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\xFF\xFF\xFF\x00\x00\x00\x21\xF9\x04\x00\x00\x00\x00\x00\x2C\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3B",
            content_type='image/jpeg'
        )
        self.depoimento = Depoimento.objects.create(
            nome= 'Atacama',
            depoimento='Lagos a 4.000 metros de altitude, formações rochosas esculpidas pelo vento, vida selvagem, superfícies que se assemelham com a da lua, lagos em que não se afunda, curiosos vilarejos, sítios arqueológicos, deserto de sal e um céu... ah, um céu de tirar o fôlego, seja de dia, quando um azul intenso toma conta, seja de noite, quando milhares de estrelas protagonizam o espetáculo. O Atacama é palco de paisagens incríveis e muito variadas, capazes de deixar os mais experientes viajantes extasiados. Quem esperaria encontrar no meio do deserto mais alto e árido do mundo um lago de águas cristalinas, cheio de flamingos? Pois no Atacama isso é possível e existe. A explicação é que uma área do deserto, chamada Salar de Atacama, tem um microclima diferente e permitiu que todas essas curiosas formações fossem possíveis. Até chuva tem nessa área, algo praticamente inexistente em um deserto como o Atacama.',
            imagem=image
        )
        self.serializer_depoimento = DepoimentoSerializer(instance = self.depoimento)
    
    def test_verifica_campos_serializados_depoimento(self):
        """Teste que verifica a serialização do modelo de Depoimento"""
        dados = self.serializer_depoimento.data
        self.assertEqual(set(dados.keys()), set(['id', 'nome', 'depoimento', 'imagem']))
    
    def test_verifica__conteudo_dos_campos_serializados_depoimento(self):
        """Teste que verifica os conteúdos serializados de Depoimento"""
        dados = self.serializer_depoimento.data
        self.assertEqual(dados['nome'], self.depoimento.nome)
        self.assertTrue(dados['depoimento'].startswith("Lagos a 4.000 metros"))
        self.assertIn("test_image", dados['imagem'])

    