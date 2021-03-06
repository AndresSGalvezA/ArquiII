;YA QUE EL PUERTO C SON LOS MENOS SIGNIFICATIVOS
;NO SE TOMARA EN CUENTA Y SE RESERVA EL PUERTO
	ORG	0X00
CONFIGURACION
	BSF	STATUS, RP0
	CLRF	TRISD		; SALIDA
	BSF	TRISA, 0 	; RA0 ENTRADA
	CLRF	TRISC 		; SALIDA
	CLRF	TRISB		; SALIDA
	BSF	ADCON1, 3
	BSF	ADCON1, 2
	BSF	ADCON1, 1
	BCF	ADCON1, 0 	; 1110 -> RA0 AN0 = ANALOGO
	BSF	ADCON1, 6	; FOSC/64
	BCF	ADCON1, 7 	; JUSTIFICACIÓN IZQUIERDA (MAS SIGINIFICATIVOS IZQUIERDA)
	BCF	STATUS, RP0
	BSF	ADCON0, 7
	BCF	ADCON0, 6 	; FOSC/64
	BCF	ADCON0, 5
	BCF	ADCON0, 4
	BCF	ADCON0, 3 	; CANAL AN0
	BSF	ADCON0, 0 	; ADC ON

START
	BSF	ADCON0, 2	; GO/DONE --> 1
ADC
	; BITS MAS SIGNIFICATIVOS MAS A LA IZQUIERDA - PORTD
	; BITS MENOS SIGNIFICATIVOS MAS A LA DERECHA (SOLO SON 2) -PORTC
	BTFSC	ADCON0, 2
	GOTO	ADC
	MOVF	ADRESH,W
	MOVWF	PORTD		;BITS MAS SIGNIFICATIVOS

	;SE HA COMENTADO YA QUE NO SE UTILIZARAN LOS BITS MENOS SIGNIFICATIVOS
	BSF	STATUS, RP0
	MOVF	ADRESL, W
	BCF	STATUS, RP0	;REGRESO AL BANCO 0
	;MOVWF	PORTC		;BITS MENOS SIGNIFICATIVOS

	;FOTO RESISTENCIA DE 4.9V Max y 0.9 Min
	;4.9V = 1003 y 0.9V = 184
	;Intervalos = (1003 - 184)/9 = 91
DISPLAY
	;SUBLW = (F - W)
	;SI LA RESTA = POSITIVA	,C=1 Z=0 F - W > 0
	;SI LA RESTA = CERO	,C=1 Z=1 F - W = 0
	;SI LA RESTA = NEGATIVA	,C=0 Z=1 F - W < 0
	;SI C = 1 -> F >= W
	MOVF	PORTD, W
	SUBLW	B'00101111'	;0 = 184  = 00 10
	BTFSS	STATUS, C
	GOTO	RNUM1	;0
	GOTO	NUM0	;1
RNUM1
	MOVF	PORTD, W
	SUBLW	B'01001111' ;1 = 275  = 01 00
	BTFSS	STATUS, C
	GOTO	RNUM2	;0
	GOTO 	NUM1	;1
RNUM2
	MOVF	PORTD, W
	SUBLW	B'01011111' ;;2 = 366  = 01 01
	BTFSS	STATUS, C
	GOTO	RNUM3	;0
	GOTO	NUM2	;1
RNUM3
	MOVF	PORTD, W
	SUBLW	B'01111111' ;3 = 457  = 01 11
	BTFSS	STATUS, C
	GOTO	RNUM4
	GOTO	NUM3
RNUM4
	MOVF	PORTD, W
	SUBLW	B'10001111' ;4 = 548  = 10 00
	BTFSS	STATUS, C
	GOTO	RNUM5
	GOTO	NUM4
RNUM5
	MOVF	PORTD, W
	SUBLW	B'10011111' ;5 = 639  = 10 01
	BTFSS	STATUS, C
	GOTO	RNUM6
	GOTO	NUM5
RNUM6
	MOVF	PORTD, W
	SUBLW	B'10111111' ;6 = 730  = 10 11
	BTFSS	STATUS, C
	GOTO	RNUM7
	GOTO	NUM6
RNUM7
	MOVF	PORTD, W
	SUBLW	B'11001111' ;7 = 821  = 11 00
	BTFSS	STATUS, C
	GOTO	RNUM8
	GOTO	NUM7
RNUM8
	MOVF	PORTD, W
	SUBLW	B'11101111' ;8 = 912  = 11 10
	BTFSS	STATUS, C
	GOTO	NUM9 ;9 = 1003 = 11 11
	GOTO	NUM8
NUM0
	MOVLW	B'00111111'
	MOVWF	PORTB
	GOTO 	FIN
NUM1
	MOVLW	B'00000110'
	MOVWF	PORTB
	GOTO	FIN
NUM2
	MOVLW	B'01011011'
	MOVWF	PORTB
	GOTO	FIN
NUM3
	MOVLW	B'01001111'
	MOVWF	PORTB
	GOTO	FIN
NUM4
	MOVLW	B'01100110'
	MOVWF	PORTB
	GOTO	FIN
NUM5
	MOVLW	B'01101101'
	MOVWF	PORTB
	GOTO	FIN
NUM6
	MOVLW	B'01111101'
	MOVWF	PORTB
	GOTO	FIN
NUM7
	MOVLW	B'00000111'
	MOVWF	PORTB
	GOTO	FIN
NUM8
	MOVLW	B'01111111'
	MOVWF	PORTB
	GOTO	FIN
NUM9
	MOVLW	B'01101111'
	MOVWF	PORTB
	GOTO	FIN
FIN
	GOTO START
	END
