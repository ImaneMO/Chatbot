# Chatbot
Python chatbot AI that helps in creating a python based chatbot with minimal coding. This provides both bots AI and chat handler and also allows easy integration of REST API's and python function calls which makes it unique and more powerful in functionality.

Installation

install from github:

    git clone git@github.com:ImaneMO/Chatbot.git
    cd Chatbot
    python setup.py install

Demo

    >>> from chatbot import demo
    >>> demo()
    Hi, how are you?
    > i'm fine
    Nice to know that you are fine
    > quit
    Thank you for talking with me.
    >>> 

Sample Code (with wikipedia search API integration)



    from chatbot import Chat,MultiFunctionCall
    import wikipedia
    def who_is(query,session_id="general"):
    try:
            return wikipedia.summary(query)
    except Except:
        for new_query in wikipedia.search(query):
           try:
                return wikipedia.summary(new_query)
            except Except:
                pass
    return "I don't know about "+query
        
    call = MultiFunctionCall({"whoIs":who_is})
    first_question="Hi, how are you?"
    Chat("examples/Example.template",call=call).converse(first_question)

