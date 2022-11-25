record = "AArch64"

cats = [
    "cats/aarch64.cat",
    "cats/aarch64-v08.cat",
    "cats/aarch64-v07.cat",
    "cats/aarch64-v06.cat",
    "cats/aarch64-v05.cat",
    "cats/aarch64-v04.cat",
    "cats/aarch64-v03.cat",
    "cats/aarch64-v02.cat",
    "cats/aarch64-v01.cat",
    "cats/aarch64-v00.cat",
    "cats/sc.cat",
    ]

cfgs = [
    "cfgs/new-web.cfg",
]

illustrative_tests = [
    "tests/MP.litmus",
    "tests/MP+dmb.sy+po.litmus",
    "tests/MP+dmb.sys.litmus",
    "tests/MP+po+dmb.sy.litmus",
    "tests/2+2W.litmus",
    "tests/2+2W+dmb.sy+po.litmus",
    "tests/2+2W+dmb.sys.litmus",
    "tests/LB.litmus",
    "tests/LB+dmb.sy+po.litmus",
    "tests/LB+dmb.sys.litmus",
    "tests/R.litmus",
    "tests/R+dmb.sy+po.litmus",
    "tests/R+dmb.sys.litmus",
    "tests/R+po+dmb.sy.litmus",
    "tests/SB.litmus",
    "tests/SB+dmb.sy+po.litmus",
    "tests/SB+dmb.sys.litmus",
    "tests/S+dmb.sy+po.litmus",
    "tests/S.litmus",
    "tests/S+po+dmb.sy.litmus",
    "tests/S+dmb.sys.litmus",
    "tests/LB+rel+BEQ.litmus",
    "tests/LB+rel+BEQ2.litmus",
    "tests/LB+rel+BEQ3.litmus",
    "tests/LB+BEQ4.litmus",
    "tests/LB+rel+CSEL.litmus",
    "tests/LB+rel+CSEL2.litmus",
    "tests/LB+rel+CSEL3.litmus",
    "tests/LB+CSEL4.litmus",
    "tests/CAS+data1.litmus",
    "tests/CAS+data2.litmus",
    "tests/LB+rel+CAS.litmus",
    "tests/MP+rel+CAS-addr.litmus",
    "tests/MP+rel+CSEL.litmus",
    "tests/MP+rel+CSEL-addr.litmus",
#    "tests/MP+CAS-rfi-ctrl+acq.litmus",
#    "tests/R+CAS+DMBLD.litmus",
#    "tests/LB+CAS-rfi-ctrl+DMBSY.litmus",
#    "tests/R+CAS-rfi-ctrl+DMBST.litmus",
#    "tests/SB+CAS-rfi-addr+DMBSY.litmus",
#    "tests/SB+SWP-rfi-addr+DMBSY.litmus",
]
