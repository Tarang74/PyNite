from numpy import where, append, array, empty, float, delete, squeeze, size

from SIprefix import si_format

class Debug():
    def debug(self):
        self.appNodes = array([['name', '0.001', '0', '0'],
                               ['name2', '0.06', '0.002', '0'],
                               ['name3', '3', '1', '1']])
        self.appMembers = array([['a', '0', '1', '0'], ['ab', '0', '2', '0']])
        self.appMaterials = array([[
            'mat1', '424325.995', '191886.999', '0.001',
            '0.00000000000675', '5', '0.0000009', ''
        ]])

    def duplicate(self, array, find):
        #---------------------------------------------------------------------#
        #                      Check if values are unique                     #
        #---------------------------------------------------------------------#
        r = False
        a = size(array, 1)
        i = 0
        while i <= len(array) - 1:
            try:
                j = 1
                while j <= a:
                    if (array[i, j] == find[j - 1]):
                        j += 1
                    else:
                        break
            except IndexError:
                if j == a:
                    r = True
            i += 1
            return r

    def maxLen(self, *argv):
        longest = 0
        for arg in argv:
            cur = len(str(arg))
            if cur > longest:
                longest = cur
        return str(longest)
    
    def debug2(self):
        x=0.001
        y=0
        z=0
        find = array([str(x), str(y), str(z)])
        dup = self.duplicate(self.appNodes, find)
        if dup == True:
            print("Error: Node coordinates must be unique.")
            print("-"*80)
            return

    def debug1(self):
        name = "Member"
        # iNode = 0
        # jNode = 1
        # material = 0

        # # Names
        # i = self.appNodes[iNode, 0]
        # j = self.appNodes[jNode, 0]
        # mat = self.appMaterials[material, 0]

        # ix = float(self.appNodes[iNode, 1])
        # iy = float(self.appNodes[iNode, 2])
        # iz = float(self.appNodes[iNode, 3])
        # jx = float(self.appNodes[jNode, 1])
        # jy = float(self.appNodes[jNode, 2])
        # jz = float(self.appNodes[jNode, 3])

        # E = float(self.appMaterials[material, 1])
        # G = float(self.appMaterials[material, 2])
        # Iy = float(self.appMaterials[material, 3])
        # Iz = float(self.appMaterials[material, 4])
        # J = float(self.appMaterials[material, 5])
        # A = float(self.appMaterials[material, 6])

        # lname = self.maxLen(name, i, j, mat)
        # lnum = self.maxLen(ix, iy, iz, jx, jy, jz)



        # print(('{:>11}: {:<' + lname + '}').format("Member name", name))

        # print(('{:>11}: {:<' + lname + '} - [{:>' + lnum + '} {}m {:>' + lnum + '} {}m {:>' + lnum + '} {}m]').format(
        #     "I-node",
        #     i,
        #     si_format(ix, precision=3, format_str=u'{value}'),
        #     si_format(ix, precision=3, format_str=u'{prefix}'),
        #     si_format(iy, precision=3, format_str=u'{value}'),
        #     si_format(iy, precision=3, format_str=u'{prefix}'),
        #     si_format(iz, precision=3, format_str=u'{value}'),
        #     si_format(iz, precision=3, format_str=u'{prefix}')))

        

        # print(('{:>11}: {:<' + lname + '} - [{:>' + lnum + '}m {:>' + lnum +
        #        '}m {:>' + lnum + '}m]').format("J-node", j, round(jx, 9),
        #                                          round(jy, 9), round(jz, 9)))
        # lnum = self.maxLen(E, G, Iy, Iz, J, A)
        # print(('{:>11}: {:<' + lname + '} - (E={:<' + lnum + '}Pa  G={:>' +
        #        lnum + '}Pa  Iy={:>' + lnum + '}m^4 Iz={:>' + lnum +
        #        '}m^4 J={:>' + lnum + '}m^4 A={:>' + lnum + '}m^2)').format(
        #            "Material", mat, round(E, 9), round(G, 9), round(Iy, 9),
        #            round(Iz, 9), round(J, 9), round(A, 9)))
    	
        x = 100000 
        y = 1
        z = 0.000001

        Iy = 0.001
        Iz = 0.00000001
        J = 0.001
        A = 0.001
        prec = 6

        lnum = self.maxLen(x, y, z)
        print(('{:>9}: {}').format("Node name", name))
        print(('{:>9}: {:>' + lnum + '} {}m^2').format("x", si_format(x, precision=3, format_str=u"{value}", p=2), si_format(x, format_str=u"{prefix}", p=2)))
        print(('{:>9}: {:>' + lnum + '} {}m^2').format("y", si_format(y, precision=3, format_str=u"{value}", p=2), si_format(y, format_str=u"{prefix}", p=2)))
        print(('{:>9}: {:>' + lnum + '} {}m^2').format("z", si_format(z, precision=3, format_str=u"{value}", p=2), si_format(z, format_str=u"{prefix}", p=2))) 

        # lnum = self.maxLen(E, G, Iy, Iz, J, A)
        # print(('{:>13}: {}').format("Material name", name))
        # print(('{:>13}: {:>' + lnum + '} {}Pa').format("E", si_format(E, precision=3, format_str=u"{value}"), si_format(E, format_str=u"{prefix}")))
        # print(('{:>13}: {:>' + lnum + '} {}Pa').format("G", si_format(G, precision=3, format_str=u"{value}"), si_format(G, format_str=u"{prefix}")))
        # print(('{:>13}: {:>' + lnum + '} {}m^4').format("Iy", si_format(Iy, precision=3, format_str=u"{value}", p=4), si_format(Iy, format_str=u"{prefix}", p=4)))
        # print(('{:>13}: {:>' + lnum + '} {}m^4').format("Iz", si_format(Iz, precision=3, format_str=u"{value}", p=4), si_format(Iz, format_str=u"{prefix}", p=4)))
        # print(('{:>13}: {:>' + lnum + '} {}m^4').format("J", si_format(J, precision=3, format_str=u"{value}", p=4), si_format(J, format_str=u"{prefix}", p=4)))
        # print(('{:>13}: {:>' + lnum + '} {}m^2').format("A", si_format(A, precision=3, format_str=u"{value}", p=2), si_format(A, format_str=u"{prefix}", p=2)))


ui = Debug()
ui.debug()
ui.debug2()

