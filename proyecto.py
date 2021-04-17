


def amortizacion():


            dinero_almacenado = float(input("elije la cantidad deseada:  "))
            plazos_de_pago = int(input("elije la cantidad de plazo deseada:  " ))
            interes_al_pagar = float(input("cantidad de interes que desearias pagar: "))
            interes = interes_al_pagar * 0.01
            plazos_de_pago_almacenado = dinero_almacenado * (((1 + interes_al_pagar) ** plazos_de_pago) * interes_al_pagar)
            plazos_de_pago_almacenado = plazos_de_pago_almacenado / (((1 + interes_al_pagar) ** plazos_de_pago) - 1)
            monto = dinero_almacenado

            cuota = "{0:.2f}".format(plazos_de_pago_almacenado)
            print ('----------------------')
            print("\n  Amortizacion:  \n")
            print('-----------------------')

            print("\nCantidad de Periodo:0/Plazos:0/Interes:0/Abono:0/maximo  de dinero prestado:{0}\n".format(monto))

            for x in range(1, plazos_de_pago + 1):
                interes = "{0:.2f}".format(float(monto) * float(interes_al_pagar))
                pago = "{0:.2f}".format(float(cuota) - float(interes))
                monto = "{0:.2f}".format(float(monto) - float(pago))

                if monto <  str (0):
                    print("gracias pudiste completar el prestamo. \n")

                print("Cantidad de Periodo:{0}/Plazos:{1}/Interes:{2}/Abono:{3}/maximo de dinero prestado:{4}\n".format(x, cuota, interes, pago, monto))

amortizacion()
print('fin del prestamo, gracias pasen buenas.')