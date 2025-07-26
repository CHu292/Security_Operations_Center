                       +----------------------+
                       |    CLIENT (Sender)   |
                       +----------+-----------+
                                  |
               Generate DH keys with each node
                                  |
                                  v
            +------------------------------------------------+
            | Encrypt data:                                 |
            |   Layer3 = Encrypt_Exit(Data)                  |
            |   Layer2 = Encrypt_Middle(Layer3)              |
            |   Layer1 = Encrypt_Entry(Layer2)               |
            +------------------------------------------------+
                                  |
                          Send Layer1 into the network
                                  |
                                  v
                          +-----------------+
                          |   Entry Node    |
                          +-----------------+
                          | Decrypt Layer1  |
                          | → forward Layer2|
                          v
                          +-----------------+
                          |   Middle Node   |
                          +-----------------+
                          | Decrypt Layer2  |
                          | → forward Layer3|
                          v
                          +-----------------+
                          |   Exit Node     |
                          +-----------------+
                          | Decrypt Layer3  |
                          | → extract Data  |
                          v
                        +--------------------+
                        |   Server receives   |
                        |       the data      |
                        +--------------------+
