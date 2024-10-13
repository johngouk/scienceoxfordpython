"""

    WebAction
    Initial attempt at a generalised action class to handle web action requests by dispatching them to
    methods for handling them. 
    Initialised with:
    -	list of target URL, method tuples
        where <method> has signature (URL, params) and returns a (URL, params) tuple, allowing for
        subs in the results pagemip

"""