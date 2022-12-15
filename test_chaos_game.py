from chaos_game import ChaosGame
from nose.tools import raises
import nose.tools as nt
import nose

@raises(ValueError)
def test_type_init():
    ChaosGame(7, 5.3)
    
@raises(ValueError)
def test_value_init():
    ChaosGame(2, 3)
    
@raises(ValueError)
def test_savepng():
    c = ChaosGame(4, 1/3)
    c.iterate(1000)
    c.savepng("outfile.txt")
    
def test_generate_ngon():
    #testing if funksjon is returning list
    c = ChaosGame(4, 1/3)
    a = c._generate_ngon(6)
    nt.assert_equal(type(a), list)

nose.run()
