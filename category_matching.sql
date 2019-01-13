DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
    IN email_p VARCHAR(40),
    IN cat1_p VARCHAR(50),
    IN cat2_p VARCHAR(50),
    IN cat3_p VARCHAR(50),
    IN email_recipient_p VARCHAR(40)
)
BEGIN
    if ( select exists (select 1 from questionaire_data where email_user = email_p) ) THEN

        select 'Username Exists !!';

    ELSE

        insert into questionaire_data
        (
            email_user,
            cat1,
            cat2,
            cat3,
            email_recipient
        )
        values
        (
            email_p,
            cat1_p,
            cat2_p,
            cat3_p,
            email_recipient_p
        );

    END IF;
END$$
DELIMITER ;
