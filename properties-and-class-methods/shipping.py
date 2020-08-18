import iso6346

class ShippingContainer:

    # class attributes
    next_serial = 1337

#    @staticmethod
#    def _get_next_serial():
#        result = ShippingContainer.next_serial
#        ShippingContainer.next_serial += 1
#        return result
    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, serial = str(serial).zfill(6))

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code,*args, **kwargs):
        return cls(owner_code, contents=None,*args, **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, items, *args, **kwargs):
        return cls(owner_code, contents=list(items), *args, **kwargs)


    def __init__(self, owner_code, contents):
        # instance attributes
        self.owner_code = owner_code
        self.contents = contents
        self.bic = self._make_bic_code(owner_code = owner_code, serial=ShippingContainer._get_next_serial())

    ## Prefixing with self than Class Name also works but the above method is more explicit and readable differentitating between class attr. vs instance attr.
    #    self.serial = self.next_serial
    #    self.next_serial += 1

class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code, 
                              serial = str(serial).zfill(6), 
                              category='R')

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32)* 5/9

    def __init__(self, owner_code, contents, celsius):
        super().__init__(owner_code, contents)
    #    if celsius > RefrigeratedShippingContainer.MAX_CELSIUS:
    #        raise ValueError("Temperature Too hot!")
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature Too hot!")
        self.celsius = value

    @property
    def fahrenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value) 