import unittest
from app.models import Pitch, User


class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''
    def setUp(self):
        self.user_John_Doe = User(username = 'John Doe', password = 'qwerty900', email = 'johndoe@gmail.com', bio = 'I love coding',
        profile_pi_path = 'https://image.tmdb.org/t/p/w500/jdjdjdjn', pitch = 'talk is cheap show me the codes')
        self.new_pitch = Pitch(pitch_id = 1234, category = 'Tech Quote', pitch_title = 'VS Code', pitch_body = 'We all love Visual Studio Code',
        postedBy = 'John Doe', user_id = 1234)

    def tearDown():
        Pitch.Clear_pitch()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))

    def test_check_intasnce_variables(self):
        self.assertEquals(self.new_pitch.pitch_id, 1234)
        self.assertSetEquals(self.new_pitch.category, 'Tech Quote')
        self.assertSetEquals(self.new_pitch.pitch_title, 'VS Code')
        self.assertSetEquals(self.new_pitch.pitch_body, 'We all love Visual Studio Code')
        self.assertSetEquals(self.new_pitch.postedBy, 'John Doe')
        self.assertSetEquals(self.new_pitch.user_id, 1234)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all() > 0))
