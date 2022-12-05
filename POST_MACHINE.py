class post_machine:

    def __init__ (self, state, write_head, tape_list):
        self.state = state
        self.write_head = write_head
        self.tape_list = tape_list

    def get_state(self):
        return self.state

    def get_write_head(self):
        return self.write_head

    def get_tape_list(self):
        return self.tape_list






