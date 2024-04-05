class Mortgage:

    def __init__(self, principal, interest, years):
        self.principal = principal
        self.interest = interest
        self.years = years
    
    def get_principal(self):
        return self.principal
    
    def get_interest(self):
        return self.interest

    def get_years(self):
        return self.years
    
    def set_principal(self, principal):
        self.principal = principal
    
    def set_interest(self, interest):
        self.interest = interest
    
    def set_years(self, years):
        self.years = years
    
    def compute_mortgage(self):
        monthly_interest=self.interest/12
        monthly_periods = self.years * 12

        return (((monthly_interest)*self.principal)*((1+monthly_interest)**monthly_periods))/(((1+monthly_interest)**monthly_periods)-1)
    
    def __repr__(self) -> str:
        return """
            Principal   : {principal}
            Interest    : {interest}
            Years       : {years}  
            """.format(principal=self.principal, interest=self.interest, years=self.years)
    
