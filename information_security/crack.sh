while read p; do
        cat $p | md5sum
        PW="password"
        # if [ $HASH == $PW ]
        # then
        #         echo $p
        # fi
        echo $HASH
done < pw.txt