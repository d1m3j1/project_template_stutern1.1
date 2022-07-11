Documentation

Important document to run
* Reading the Data
* Handling Missing Values
* Feature Engineering / Modeling II 
    * In the pipeline, if the OrdinalEnc2() transformer is not commented out, the error ~AttributeError: 'numpy.ndarray' object has no attribute 'apply' isn't there~
    * However we have this error if the OrdinalEnc2() is commented out we have this error

    ~TypeError: ufunc 'isnan' not supported for the input types, and the inputs could not be safely coerced to any supported types according to the casting rule ''safe''
    is still encountered.~
    when we try to run a prediction. 

In a nut shell, both errors are still encountered.

