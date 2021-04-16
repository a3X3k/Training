#!/bin/sh

xxd Twin1 > Twin1.hex
xxd Twin2 > Twin2.hex

xxd Twin1 | grep 0023b990
xxd Twin2 | grep 0023b990

echo ""

xxd Twin1 | grep 0023be20
xxd Twin2 | grep 0023be20

echo ""

xxd Twin1 | grep 0023c200
xxd Twin2 | grep 0023c200

echo ""

xxd Twin1 | grep 0023c640
xxd Twin2 | grep 0023c640

echo ""

xxd Twin1 | grep 0023c960
xxd Twin2 | grep 0023c960

echo ""

xxd Twin1 | grep 0023ce50
xxd Twin2 | grep 0023ce50

echo ""

xxd Twin1 | grep 0023d3c0
xxd Twin2 | grep 0023d3c0

echo ""

xxd Twin1 | grep 0023d830
xxd Twin2 | grep 0023d830

echo ""

xxd Twin1 | grep 0023dca0
xxd Twin2 | grep 0023dca0

echo ""

xxd Twin1 | grep 0023dfd0
xxd Twin2 | grep 0023dfd0

echo ""

xxd Twin1 | grep 0023e620
xxd Twin2 | grep 0023e620

echo ""

xxd Twin1 | grep 0023eab0
xxd Twin2 | grep 0023eab0

echo ""

xxd Twin1 | grep 0023f190
xxd Twin2 | grep 0023f190

echo ""

xxd Twin1 | grep 0023f6d0
xxd Twin2 | grep 0023f6d0

echo ""

xxd Twin1 | grep 0023fb90
xxd Twin2 | grep 0023fb90

echo ""

xxd Twin1 | grep 00240020
xxd Twin2 | grep 00240020
