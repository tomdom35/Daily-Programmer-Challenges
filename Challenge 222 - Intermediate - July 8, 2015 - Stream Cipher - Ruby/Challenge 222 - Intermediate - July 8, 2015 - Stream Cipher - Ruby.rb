def enc(msg, key)
    key_stream = [key]
    cipher_text = ""
    for i in 0..msg.length-1
        key_stream << (78475*(key_stream[i])+3948)%128
        cipher_text << (key_stream[i+1]^msg[i].ord).ord
    end
    return cipher_text
end

def dec(cipher_text, key)
    return enc(cipher_text,key)
end

key = 14226
msg = "Attack at dawn!"
cipher_text = enc(msg, key)
plain_text = dec(cipher_text,key)
puts "Original Message: #{msg}"
puts "Cipher Text: #{cipher_text}"
puts "Plain Text: #{plain_text}"