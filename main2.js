let Peer = require("simple-peer")
let socket = io()
const video = document.querySelector("video")
let client = {}

navigator.mediaDevices.getUserMedia({video:true,audio:true})
.then(stream => {
    socket.emit("NewClient")
    video.srcObject = stream
    video.play()

    function initPeer(type) {
        let peer = new Peer({initiator:(type == "init")?true:false,stream:stream,trickle:false})
        peer.on("stream",(stream)=>{
            CreateVideo(stream)
        })
        peer.on("close",()=>{
            document.getElementById("peerVideo").remove()
            peer.destroy()
            console.log("vay canına")
        })
        return peer
    }
    function MakePeer() {
        client.gotAnswer = false
        let peer = initPeer("init")
        peer.on("signal",(data)=>{
            if (!client.gotAnswer) {
                socket.emit("Offer",data)
            }
        })
        client.peer = peer
    }
    function FrontAnswer(offer){
        let peer = initPeer("notInit")
        peer.on("signal",(data)=>{
            socket.emit("Answer",data)
        })
        peer.signal(offer)
    }
    function SignalAnswer(Answer) {
        client.gotAnswer = true
        let peer = client.peer
        peer.signal(Answer)
    }
    function CreateVideo(stream) {
        let video = document.createElement("video")
        video.id = "peerVideo"
        video.srcObject = stream
        video.autoplay = true
        video.className = "video-chat-other"
        document.querySelector("body").appendChild(video)
        console.log("Vay cannına")
    }
    function SessionActive() {
        document.write("Session Active")
    }
    socket.on("BackOffer",FrontAnswer)
    socket.on("BackAnswer",SignalAnswer)
    socket.on("SessionActive",SessionActive)
    socket.on("CreatePeer",MakePeer)
})
.catch(err => {document.write(err)})
