from block import BlockEntity,Block
from Biskit.fret.fretentity import FRETEntity
from Biskit.fret.chromophore import Chromophore
from Biskit.PDBModel import PDBModel
from interval import Interval
from protein import Protein

class PolyChromophore ( BlockEntity , Chromophore):
    """"
    Wrapper for Chromophore. Please see Chromophore for further information.
    """
    
    def __init__(self,name,source, prot,database):
        """
        Creation (see Chromophore and BlockEntity for further info.).
        """
        BlockEntity.__init__(self,name,prot)
        Chromophore.__init__(self,name,source,database)
        
    def getStructData(self,atoms):
        return self.structure.take(atoms)
        

class PolyFRETEntity(BlockEntity , FRETEntity):
    """"
    Wrapper for FRETEntity. Please see FRETEntity for further information.
    """
    
    
    """Path for structures (pdb files) """
    PROTEIN_STRUCTURE_SOURCE_DIR = "./"
    
    
    def __init__(self,name,path = "./"):
        """
        Creation (see Chromophore and BlockEntity for further info.).
        """
        
        FRETEntity.__init__(self,name,chromo_autodef = False, database = "../fret/"+FRETEntity.DEFAULT_DB)
    
        p = Protein(path+self.source+".pdb")
        
        self.structure = p
        
        BlockEntity.__init__(self,name,self.structure)
        
        self.chromo = PolyChromophore (self.name,source = self.source,database="../fret/"+Chromophore.DEFAULT_DB ,prot= p)
        
    
    def onInsertion(self,myassembly=None):
        """
        See BlockEntity::onInsertion
        """
        
        c = Block(self.chromo.name+"_Chromophore",father=myassembly.blocks[-1],entity=self.chromo)
        c.addInterval(self.chromo.atomrange[0],self.chromo.atomrange[1])
        myassembly.addBlock(c)
    
    def getStructData(self,atoms):
        return self.structure
        
    

##############
## Test
##############
import Biskit.test as BT
import Biskit.tools as T
from assembly import Assembly 
from block import Block

class Test(BT.BiskitTest):
    """ Test cases for Polyfret"""
    
    def prepare(self):
        pass

    def cleanUp( self ):
        pass
    
    def test_Entity(self):
        """Polyfret test cases"""
        p = PolyFRETEntity("mCitrine")
        a = Assembly()
        b = Block("my_mCitrine",entity = p)
        a.addBlock(b)
        if self.local:
            print a
            
        #check the creation
        self.assertEqual( len(a.blocks),2)
        self.assertEqual( a.blocks[0].name,"my_mCitrine")
        self.assertEqual( a.blocks[1].name,"mCitrine_Chromophore")
        
        #if fretentity and chromophore pass their tests then everithing is correct
        
if __name__ == '__main__':

    BT.localTest()