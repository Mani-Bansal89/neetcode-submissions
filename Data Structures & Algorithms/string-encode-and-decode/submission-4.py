class Solution:
    def get_ascii(self, char):
        ascii_char = str(ord(char))
        return ascii_char.zfill(3)

    def encode(self, strs: List[str]) -> str:
        s = ''
        for val in strs:
            for char in val:
                s += self.get_ascii(char)
            s += '300'
        return s

    def decode(self, s: str) -> List[str]:
        output = []
        encoded_s = ''
        for i in range(0,len(s),3):
            ascii_char = int(s[i:i+3])
            if ascii_char == 300:
                output.append(encoded_s)
                encoded_s = ''
            else:
                encoded_s += chr(ascii_char)
        return output
    
