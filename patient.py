class Patient():

   def __init__(self, name, id, bp_hi, bp_lo):
      self.name  = name
      self.id    = id
      self.bp_hi = bp_hi
      self.bp_lo = bp_lo
      self.medicine = []
   
   def update_name(self,new_name):
      self.name = new_name

   def update_id(self,new_id):
      self.id = new_id

   def update_bp_hi(self,new_bp_hi):
      self.update_bp_hi = new_bp_hi

   def update_bp_lo(self,new_bp_lo):
      self.update_bp_lo = new_bp_lo
   
